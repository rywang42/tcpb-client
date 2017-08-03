/** \file tcpb.h
 *  \brief Definition of TCPBClient class
 *  \author Stefan Seritan <sseritan@stanford.edu>
 *  \date Jul 2017
 */

#ifndef TCPB_H_
#define TCPB_H_

#include <string>

#include "terachem_server.pb.h"

#ifndef MAX_STR_LEN
#define MAX_STR_LEN 1024
#endif

/**
 * \brief TeraChem Protocol Buffer (TCPB) Client class
 * Handles communicating with a TeraChem server through sockets and protocol buffers
 * Based on protobufserver.cpp/.h in the TeraChem source code and tcpb.py (that came first)
 * Direct control of the asynchronous server communication is possible,
 * but the typical use would be the convenience functions like ComputeEnergy()
 *
 * One major difference to the TCPB server code is that the client only needs one active connection
 * This removes most threading and select logic (but limits communication to one server)
 * However, timeouts do need to be explicitly set on the socket
 **/
class TCPBClient {
  public:
    //Constructor/Destructor
    /**
     * Constructor for TCPBClient class
     *
     * @param host C string of hostname with TCPB server
     * @param port Integer port of TCPB server
     **/
    TCPBClient(const char* host,
               int port);

    /**
     * Destructor for TCPBClient
     * Handles disconnect and logfile cleanup
     **/
    ~TCPBClient();

    /***********************
     * JOB INPUT (SETTERS) *
     ***********************/
    /**
     * Set the atom types in the JobInput Protocol Buffer
     *
     * @param atoms Array of C strings for atom types
     * @param num_atoms Integer number of entries in atoms
     **/
    void SetAtoms(const char** atoms,
                  const int num_atoms);

    /**
     * Set the charge in the JobInput Protocol Buffer
     *
     * @param charge Molecular charge
     **/
    void SetCharge(const int charge);

    /**
     * Set the spin multiplicity in the JobInput Protocol Buffer
     *
     * @param spinMult Spin multiplicity
     **/
    void SetSpinMult(const int spinMult);

    /**
     * Set closed or open shell in the JobInput Protocol Buffer
     *
     * @param closed If True, the system is set as closed shell
     **/
    void SetClosed(const bool closed);

    /**
     * Set restricted or unrestricted in the JobInput Protocol Buffer
     *
     * @param restricted If True, the system is set as restricted
     **/
    void SetRestricted(const bool restricted);

    /**
     * Set the TeraChem method in the JobInput Protocol Buffer
     * Will error out if not a valid TeraChem method (as defined in the .proto)
     *
     * @param method C string of method name (case insensitive)
     **/
    void SetMethod(const char* method);

    /**
     * Set the TeraChem basis set in the JobInput Protocol Buffer
     * Will error out if not a valid TeraChem basis set (as defined in the .proto)
     *
     * @param basis C string of basis set name (case insensitive)
     **/
    void SetBasis(const char* basis);

    /************************
     * SERVER COMMUNICATION *
     ************************/
    /**
     * Initialize the server_ socket and connect to the given host (host_) and port (port_)
     **/
    void Connect();

    /**
     * Disconnect and discard the server_ socket
     **/
    void Disconnect();

    /**
     * Checks whether the server is available (does not reserve server)
     *
     * @return True if server has no running job, False otherwise
     **/
    bool IsAvailable();

    /**
     * Send the JobInput Protocol Buffer to the TCPB server
     * Send is blocking, but function will not wait for job completion (thus job is asynchronous)
     *
     * @param runType TeraChem run type, as defined in the JobInput_RunType enum 
     * @param geom Double array of XYZs for each atom
     * @param num_atoms Integer number of atoms stored in geom
     * @param unitType Geometry units, as defined in the Mol_UnitType enum
     * @return True if job was submitted, False if server was busy
     **/
    bool SendJobAsync(const terachem_server::JobInput_RunType runType,
                      const double* geom,
                      const int num_atoms,
                      const terachem_server::Mol_UnitType unitType);
    bool SendJobAsync();
    bool CheckJobAsync(); //STUB
    bool RecvJobAsync(); //STUB

    // Convenience Functions
    void ComputeJobSync(); //STUB
    void ComputeEnergy(double& energy); //STUB
    void ComputeGradient(double& energy, double* gradient); //STUB

  private:
    char host_[MAX_STR_LEN];
    int port_;
    int server_;
    FILE* clientLogFile_;
    // Protocol buffer variables
    terachem_server::JobInput jobInput_;
    terachem_server::JobOutput jobOutput_;
    // State variables, ensuring everything is set prior to 
    bool atomsSet, chargeSet, spinMultSet, closedSet, restrictedSet, methodSet, basisSet;

    /***************************
     * SOCKET HELPER FUNCTIONS *
     ***************************/
    // TODO: These should probably be split out, pretty independent
    // TODO: These functions will not work on Windows at the moment
    /**
     * A high-level socket recv with error checking and clean up for broken connections
     *
     * @param buf Buffer for incoming packet
     * @param len Byte size of incoming packet
     * @param log String message to be printed out as part of SocketLog messages (easier debugging)
     * @return status True if recv'd full packet, False otherwise (indicating server_ socket is now closed)
     **/
    bool HandleRecv(char* buf,
                    int len,
                    const char* log);

    /**
     * A high-level socket send with error checking and clean up for broken connections
     *
     * @param buf Buffer for outgoing packet
     * @param len Byte size of outgoing packet
     * @param log String message to be printed out as part of SocketLog messages (easier debugging)
     * @return status True if sent full packet, False otherwise (indicating server_ socket is now closed)
     **/
    bool HandleSend(const char* buf,
                    int len,
                    const char* log);

    /**
     * A low-level socket recv wrapper to ensure full packet recv
     *
     * @param buf Buffer for incoming packet
     * @param len Byte size of incoming packet
     * @return nsent Number of bytes recv'd
     **/
    int RecvN(char* buf,
              int len);

    /**
     * A low-level socket send wrapper to ensure full packet send
     *
     * @param buf Buffer for outgoing packet
     * @param len Byte size of outgoing packet
     * @return nsent Number of bytes sent
     **/
    int SendN(const char* buf,
              int len);

    /**
     * Verbose logging with timestamps for the client socket into "client.log"
     * This function is similar to fprintf(clientLogFile_, format, ...) with SOCKETLOGS defined
     * This function does nothing without SOCKETLOGS defined
     *
     * @param format Format string for vfprintf
     * @param va_args Variable arguments for vfprintf
     **/
    void SocketLog(const char* format, ...);
};

#endif

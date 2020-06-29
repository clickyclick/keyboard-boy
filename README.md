# keyboard-boy
Key logger, only to be used justly. 

Server listens for UDP packets, client sends each key pressed as a UDP packet.

## Setup

### Client
    Due to the nature of keyloggers we want to generate an exe that we can run without any Python dependancies.
    We achieve this by using (insert tool here) to build the exe that can be more portable.

    To run the keylogger simply execute the exe file in the payload folder.

    NOTE: hostname and port are hardcoded as we are building an exe from python directly


### Server
    To run the server, simply run 
    python3 src/server.py <PORTNUMBER>

    go to logs/ to see the output



## License 


MIT License

Copyright (c) 2020 Aidan Wilson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Aidan Wilson bears no responsibility for use of this software, this project was
created for the sole purpose of education and learning.

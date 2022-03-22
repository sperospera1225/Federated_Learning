import grpc
import os
import sys
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2
import numpy as np
import base64

class UnaryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = '117.17.189.215'
        self.server_port = 27000

        # instantiate a channel
        self.channel = grpc.insecure_channel(
                '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.UnaryStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.Message(message=message)
        print(f'{message}')
        return self.stub.GetServerResponse(message)


if __name__ == '__main__':
    filename = input('전송할 파일 이름을 입력하세요: ')
    client = UnaryClient()
    result = client.get_url(message=str(filename))

    message = base64.b64decode(result.message)
    input_arr = np.frombuffer(message, dtype=np.float32).reshape(1, 16, 5, 5)
    print(input_arr)
    print(input_arr.shape)
    np.save('./input_arr.npy', input_arr)
    #nowdir = os.getcwd()
    #with open(nowdir+"/"+filename, 'wb') as f:
    #    f.write(result)

    #print(f'{len(input_arr)}')
~                              

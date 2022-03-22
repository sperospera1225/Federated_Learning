import grpc
from concurrent import futures
import time
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2
from os.path import exists
import sys
import numpy as np
import base64

class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):

        # get the string from the incoming request
        filename = request.message
        
        if not exists(filename):
            print("no file")
            sys.exit()
        print("파일 %s 전송 시작" %filename)
        
        data = np.load('./input_arr.npy')
        data = data[:1,:,:,:]
        data = base64.b64encode(data)
        return_data = pb2.MessageResponse(message = data)
        
        return return_data


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port('[::]:27000')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

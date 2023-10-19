import greet_pb2_grpc
import greet_pb2
import time
import grpc

def get_client_stream_requests():
    while True:
        name = input("Please enter a name (or nothing to stop chatting): ")
        greet = input("Please enter a greeting: ")
        print()
        if name == "":
            break
        payload = {
            "name": name,
            "greeting":greet
        }
        hello_request = greet_pb2.HelloRequest(**payload)
        yield hello_request
        time.sleep(1)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        # print("1. SaysHello - Unary")
        # print("2. ParrotSaysHello - Server Side Streaming")
        # print("3. ChattyClientSaysHello - Client Side streaming")
        # print("4. SayHello - Both")
        
        # rpc_call: int = int(input("Which rpc would you like to make: "))
        # if rpc_call == 1:
        #     payload = {
        #         "greeting":"Hi",
        #         "name":"Shameel"
        #     }
        #     hello_request = greet_pb2.HelloRequest(**payload)
        #     hello_reply = stub.SayHello(hello_request)
        #     print("SayHello Response Recieved")
        #     print(hello_reply)
        #     # print(type(hello_reply))
        # if rpc_call == 2:
        #     payload = {
        #         "greeting": "Molweni",
        #         "name": "Xhosa guy"
        #     }
        #     hello_request = greet_pb2.HelloRequest(**payload)
        #     hello_replies = stub.ParrotSaysHello(hello_request)
        #     for hell_reply in hello_replies:
        #         print("ParrotSaysHello Response Recied:\n")
        #         print(hell_reply)
                
        # if rpc_call == 3:
        #     hello_reply = stub.ChattyClientSaysHello(get_client_stream_requests())
        #     print()
        #     print("ChattyClientSaysHello Response recieved")
        #     print(f"SERVER: {hello_reply}")
        #     print()

        # if rpc_call == 4:
        responses = stub.InteractingHello(get_client_stream_requests())
        
        for response in responses:
            print("Response Received from the server")
            print(response)

if __name__ == "__main__":
    run()

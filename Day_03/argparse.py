import argparse 



parser = argparse.ArgumentParser( 
    description="Provide personal greeting"
) 

parser.add_argument( # add one atribute to the parser, list
    "-n", "--name", metavar="name",
    required=True, help="Add your name to greet"
)

args = parser.parse_args()

message = f"hello {args.name}!"

print(message) 
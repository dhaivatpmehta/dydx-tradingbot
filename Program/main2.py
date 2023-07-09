from func_connections import connect_dydx
from func_private import abort_all_positions

if __name__ == "__main__":
  
    #Connect to client
   try : 
    print("Connecting to Client...")
    client = connect_dydx()
   except Exception as e:
      print(e) 
      print("Error connecting to client: ", e)
      exit(1)
#ABORT ALL OPEN POSITIONS
if abort_all_positions:
   try:
      print("closing all position")
      close_orders = abort_all_positions(client)
   except Exception as e:
      print("error closing all position ",e)
      exit(1)
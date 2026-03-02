from flask import Flask
import requests, argparse, routine

api_url = "https://exercisedb.dev"

# Create a Flask instance
#app = Flask(__name__)

#@app.route("/", methods=["POST"])
#def add_expense():



def get_workout_info(exerciseId):
    #url = f"{api_url}/api/v1/exercises/{exerciseId}"
    url = f"{api_url}/api/v1/exercises"
    response = requests.get(url)
    print(response.json())
    #print("DATA")
    #print(response.json()["data"])
    #print("NAME")
    #print(response.json()["data"]["name"])
    #print("TARGET MUSCLES")
    #print (response.json()["data"]["targetMuscles"])


#routine.add_routine("Push")    


get_workout_info("ztAa1RK")   
#parser = argparse.ArgumentParser(description= "adds an expense")
#parser.add_argument("description", type=str)
#parser.add_argument("amount", type=float)
#args = parser.parse_args()
#(expense.add_expense(args.description, args.amount))

# Run the Flask app if this file is executed directly
#if __name__ == "__main__":
#    app.run(debug=True)

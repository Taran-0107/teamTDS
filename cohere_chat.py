import cohere

# Initialize the client with your API key
api_key = "Tf8dnum5fzGEw1BWkPu1aAJ91cgDtjSJTS6WCzYI"

def init_client():
    co = cohere.ClientV2(api_key)
    return co

def fetch_response(client,messages):
    # Generate text
    co=client
    response = co.chat_stream(
        model="command-r-plus-08-2024",
        messages=messages,
    )

    response_text=""
    for event in response:
        if event.type == "content-delta":
            token=event.delta.message.content.text
            response_text+=token
            print(token, end="")

    return response_text



if __name__ =="__main__":

    c=init_client()
    prompt="tell me about water"
    t=fetch_response(c,[{"role":"user","content":prompt}])

    # print("______________-sepertor______________")

    #print(t)

command = ''
started = False
while True:
    command = input("type help to learn about the game: ").lower()
    if command == 'start':
        if started:
            print('Car already started.')
        else:
            started = True
            print('Car started...')
    elif command == 'stop':
        if not started:
            print('Car already stopped.')
        else:
            started = False
            print('Car stopped.')
    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car  
quit - to exit
        ''')
    elif command == 'quit':
        print('Goodbye!')
        break
    else:
        print("I don't understand that...")
        
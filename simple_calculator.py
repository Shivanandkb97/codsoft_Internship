while True:
  print("\nOptions:")
  print("Enter '1' for addition")
  print("Enter '2' for subtraction")
  print("Enter '3' for multiplication")
  print("Enter '4' for division")
  print("Enter '5' to end the program")

  user_input = input("Enter your choice: ")

  if user_input in ["1", "2", "3", "4"]:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if user_input == "1":
      print("Result: ", num1 + num2)
    elif user_input == "2":
      print("Result: ", num1 - num2)
    elif user_input == "3":
      print("Result: ", num1 * num2)
    elif user_input == "4":
      if num2 != 0:
        print("Result: ", num1 / num2)
      else:
        print("Division not possible when the denominator is zero.")
  elif user_input == "5":
    print("Thank you!")
    break
  else:
    print("Invalid input. Please enter a valid option.")

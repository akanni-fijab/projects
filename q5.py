def main():
    # print("I reached here")
    time_of_day = input("What time is it ? ")


    if 7.0 <= convert(time_of_day)<= 8.0:
         print("breakfast time")
    elif 12.0 <= convert(time_of_day) <=13.0:
        print("lunch time")

    elif 18.0 <= convert(time_of_day) <=19.0:
        print("dinner time")



def convert(time):
    hours,minutes = time.split(":")

    hours= int(hours)
    minutes = int(minutes) / 60
    float_sum = hours + minutes
    return float_sum



if __name__ == "__main__":
    main()



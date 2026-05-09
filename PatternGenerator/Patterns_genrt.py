import random
Run_Number = 0
Training_Runs = int(input("How many patterns do you want to generate? "))
while Run_Number < Training_Runs:
    def StraightLine_Pattern(diff,end,start):
        count = 0
        val=[] 
        while count < end:
                val.append(start)
                start += diff
                count+=1
        return val

    def add_pattern(Val_Pattern):
        with open(r"D:\PatternGenerator\Patterns.txt", "a+") as file:
            file.seek(0)
            content = set(file.read().splitlines())
            pattern_string = ",".join(map(str, Val_Pattern))
            if pattern_string in content:
                print("Pattern already exists")
            else:
                file.write(pattern_string + "\n")


    def random_number_gen():
        RandomX = random.randint(1,10)
        return RandomX

    def Check_Val():
            
                    Diff = random_number_gen()
                    End = random_number_gen()
                    Start = random_number_gen()
                    if Start >  End:
                        x= Start
                        Start = End
                        End = x
                    print(f"Start: {Start} End: {End} Diff: {Diff}")
                    return StraightLine_Pattern(Diff, End, Start)             
    Val_Pattern = Check_Val()
    add_pattern(Val_Pattern)
    Run_Number += 1      
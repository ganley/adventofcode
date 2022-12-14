package main

import (
    "bufio"
    "fmt"
    "os"
)

func main() {
    var s int = 0

    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() {
        switch scanner.Text() {
        case "A X":     // rock vs rock -> tie
            s += 1 + 3
        case "B X":     // paper vs rock -> loss
            s += 1 + 0
        case "C X":     // scissors vs rock -> win
            s += 1 + 6
        case "A Y":     // rock vs paper -> win
            s += 2 + 6
        case "B Y":     // paper vs paper -> tie
            s += 2 + 3
        case "C Y":     // scissors vs paper -> loss
            s += 2 + 0
        case "A Z":     // rock vs scissors -> loss
            s += 3 + 0
        case "B Z":     // paper vs scissors -> win
            s += 3 + 6
        case "C Z":     // scissors vs scissors -> tie
            s += 3 + 3
        }
    }

    fmt.Println(s)
}


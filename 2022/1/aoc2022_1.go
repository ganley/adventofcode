package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
)

func main() {
    var s int = 0
    var m int = 0

    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() {
	    if len(scanner.Text()) == 0 {
            if s > m {
                m = s
            }
            s = 0
        } else {
            i, _ := strconv.Atoi(scanner.Text())
            s += i
        }
    }

    fmt.Println(m)
}


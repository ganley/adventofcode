package main

import (
    "bufio"
    "fmt"
    "os"
    "regexp"
    "strconv"
)


func main() {
    var re = regexp.MustCompile("[-,]")
    var c = 0

    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() {
        var t = re.Split(scanner.Text(), 4)
        var s0, _ = strconv.Atoi(t[0])
        var e0, _ = strconv.Atoi(t[1])
        var s1, _ = strconv.Atoi(t[2])
        var e1, _ = strconv.Atoi(t[3])
        if (s0 <= s1 && s1 <= e0) || (s0 <= e1 && e1 <= e0) || (s1 <= s0 && s0 <= e1) || (s1 <= e0 && e0 <= e1) {
            c++
        }
    }

    fmt.Println(c)
}


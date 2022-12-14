package main

import (
    "bufio"
    "fmt"
    "os"
)


func priority(c byte) int {
    if c >= 'a' && c <= 'z' {
        return int(c) - int('a') + 1
    }
    return int(c) - int('A') + 27
}


// c is an array of items
// each element has bit 0, 1, and 2 set according to whether that item
// was contained in that elf index of each group of 3
// we're looking for the element that is in all 3 packs in each group of 3

func main() {
    var s int = 0
    var line = 0
    var c[128] int

    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() {
        var t = scanner.Text()
        for i := 0; i < len(t); i++ {
            var ix = int(t[i])
            c[ix] |= 1 << (line % 3)
        }

        line++
        if line % 3 == 0 {
            for i := 0; i < 128; i++ {
                if c[i] == 7 {
                    s += priority(byte(i))
                }
                c[i] = 0
            }
        }
    }

    fmt.Println(s)
}


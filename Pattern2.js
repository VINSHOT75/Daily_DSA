// print following pattern
//      *
//      **
//      ***
//      ****
//      *****


n = 5
let i = 1

while (i <= n) {
    let j = 1
    while (j <= i) {
        process.stdout.write("*")
        j = j +1
    }
    i = i + 1
    console.log()
}
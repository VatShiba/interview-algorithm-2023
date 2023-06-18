function is_power_of_two(n) {
    if (n < 1) return false
    while (n > 1) {
        if (n % 2 !== 0) return false
        n = n / 2
    }
    return true
}

function is_power_of_two_bitwise(n) {
    if (n < 1) return false
    return (n & n - 1) === 0
}

// :) // :) // :) //

console.log("For Loop: Time Complexity is O(log n)")
for (let i = 1; i <= 100; i++) {
    console.log(`The number ${i} is ${is_power_of_two(i) ? "" : "not "}power of two`)
}

console.log("Bitwise: Time Complexity is O(1)")
for (let i = 1; i <= 100; i++) {
    console.log(`The number ${i} is ${is_power_of_two_bitwise(i) ? "" : "not "}power of two`)
}
func isAnagram(s string, t string) bool {
    charSMap := make(map[rune]int)
    charTMap := make(map[rune]int)
    
    if len(s) != len(t) {
        return false
    }

    for i := 0; i < len(s); i++ {
        charS := rune(s[i])
        charT := rune(t[i])
        charSMap[charS]++
        charTMap[charT]++
    }
    for char := range charSMap {
        if charSMap[char] != charTMap[char] {
            return false
        }
    }
    return true
}

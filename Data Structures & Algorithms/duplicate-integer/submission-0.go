func hasDuplicate(nums []int) bool {
   contains := make(map[int]bool)
   for _,num := range nums {
    if _,ok := contains[num]; ok {
        return true
    } else {
        contains[num] = true
    }
   }
   return false
}

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
    /* BRUTE FORCE SOLUTION O(n^2)
        for(int i=0;i<nums.size();i++){
            for(int j=0;j<nums.size();j++){
                if(nums[i] == nums[j] && i != j){
                    return true;
                }
            }
        }
        return false; */
    /* Another solution - sort array first O(nlogn)
        int n = nums.size();
        bool = swapped;
        for(int i=0;i<n-1;i++){
            swapped = false;
            for(int j=0;j<n-1-i;j++){
                if (nums[j] > nums[j+1]){
                    int temp = nums[j];
                    nums[j] = nums[j+1];
                    nums[j+1] = temp;
                    swapped = true;
                }
            }
            if(!swapped){
                break;
            }
        } */
    //PATERN - HASH USAGE O(n)
        unordered_set<int> hash;
        for(int n : nums){
            if(hash.contains(n)){
                return true;
            }else{
                hash.insert(n);
            }
        }
        return false;
    }
};
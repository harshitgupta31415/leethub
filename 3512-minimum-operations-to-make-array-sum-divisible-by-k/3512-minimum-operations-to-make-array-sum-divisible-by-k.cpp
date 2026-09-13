class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        // int n=0;
        // for (int i ; i<nums.size() ; i++){
        //     n+=nums[i];
        //     n%=k;
        // }
        return accumulate(nums.begin(), nums.end(), 0)%k;
    }
};
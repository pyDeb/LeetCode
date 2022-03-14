

bool search(int *nums, int numsSize, int target)
{
    int i = 0;
    int *sorted_arr;
    bool rotated = false;
    while(i < numsSize - 1)
    {
        // we get the pivot point here
        if(nums[i] > nums[i + 1])
        {
            rotated = true;
            break;
        }

        i++;
    }
    if(rotated)
    {
       // copy everything from pivot until the end
       sorted_arr = malloc(numsSize * sizeof(int));
       for(int j = 0, k= i + 1; k < numsSize; j++, k++)
            sorted_arr[j] = nums[k];
       // copy the pivoted area to the end of sorted_arr
       for(int j = numsSize - i - 1, k = 0; k <= i; k++, j++)
            sorted_arr[j] = nums[k];

       int start = 0;
       int end = numsSize - 1;

       while(start <= end)
       {
            int middle = (end + start)/2;
            if(target == sorted_arr[middle])
                return true;

            if(target > sorted_arr[middle])
                start = middle + 1;

            if(target < sorted_arr[middle])
                end = middle - 1;

            continue;
       }
    }
    else
    {
       int start = 0;
       int end = numsSize - 1;

       while(start <= end)
       {
            int middle = (end + start)/2;
            if(target == nums[middle])
                return true;

            if(target > nums[middle])
                start = middle + 1;

            if(target < nums[middle])
                end = middle - 1;

            continue;
    }
    }

    return false;
}

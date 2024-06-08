function [d_min,path_min]=dp_min(d,start,pick,throw)
[validPermutations]=perm(start,pick,throw);
dis=[];
for a=1:size(validPermutations,1)
    diss=0;
    for b=1:size(validPermutations(a,:),2)-1
        c=validPermutations(a,b);f=validPermutations(a,b+1);
        diss=diss+d(c,f);
    end
    dis=[dis;diss];
end    
[val,index] = min(dis);
d_min=val;
path_min=validPermutations(index,:);
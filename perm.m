function [validPermutations]=perm(start,pick,throw)
start=[0];
pick=[1,3,5,7,9];
throw=[2,4,6,8,10];
numbers=[start,pick,throw];
allPermutations = perms(numbers(2:end));
validPermutations = [];

for i = 1:size(allPermutations, 1)
    permutation = [allPermutations(i, :)];
    pairsToCompare=[];
    for k=1:size(pick,2)    
        pairsToCompare =  [pairsToCompare;pick(k),throw(k)];
    end
    allConditionsMet = true;
    for j = 1:size(pairsToCompare, 1)
        firstNumber = pairsToCompare(j, 1);
        secondNumber = pairsToCompare(j, 2);
        index1=find(permutation==firstNumber);
        index2=find(permutation==secondNumber);
        if index1 > index2
            allConditionsMet = false;
            break;
        end
    end
    if allConditionsMet
        validPermutations = [validPermutations; start,permutation];
    end
end
disp('满足条件的排列组合形式：');
disp(validPermutations);
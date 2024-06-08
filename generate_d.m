function [d]=generate_d(W)
n=size(W,1);
d=W;
p=zeros(n,n);
for j=1:n;
    p(:,j)=j;
end
for k=1:n
    for i=1:n
        for j=1:n
            if d(i,j)>d(i,k)+d(k,j)
                d(i,j)=d(i,k)+d(k,j);
                p(i,j)=p(i,k);
            end
        end
    end
end    
M=inf;
W=[0	6	M	17	M	M	M	M	7	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M;
6	0	2	M	M	1	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M;
M	2	0	M	M	M	2	8	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M;
17	M	M	0	7	M	M	M	M	M	M	M	M	M	M	M	M	11	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M;
M	M	M	7	0	M	M	M	M	M	M	M	6	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M;
M	1	M	M	M	0	1	M	M	3	3	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M;
M	M	2	M	M	1	0	6	M	M	M	2	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M;
M	M	8	M	M	M	6	0	M	M	M	M	M	M	M	M	M	M	M	M	M	M	10	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M;
7	M	M	M	M	M	M	M	0	2	M	M	M	4	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M;
M	M	M	M	M	3	M	M	2	0	2	M	M	M	3	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M;
M	M	M	M	M	3	M	M	M	2	0	4	M	M	M	2	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M;
M	M	M	M	M	M	2	M	M	M	4	0	M	M	M	M	2	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M;
M	M	M	M	6	M	M	M	M	M	M	M	0	2	M	M	M	M	4	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M;
M	M	M	M	M	M	M	M	4	M	M	M	2	0	1	M	M	M	M	M	M	M	M	M	M	7	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M;
M	M	M	M	M	M	M	M	M	3	M	M	M	1	0	1	M	M	M	M	M	M	M	M	M	M	8	M	M	M	M	M	M	M	M	M	M	M	M	M	M;
M	M	M	M	M	M	M	M	M	M	2	M	M	M	1	0	3	M	M	3	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M;
M	M	M	M	M	M	M	M	M	M	M	2	M	M	M	3	0	M	M	M	2	4	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M;
M	M	M	11	M	M	M	M	M	M	M	M	M	M	M	M	M	0	2	M	M	M	M	3	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M;
M	M	M	M	M	M	M	M	M	M	M	M	4	M	M	M	M	2	0	M	M	M	M	M	2	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M;
M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	3	M	M	M	0	1	M	M	M	M	M	M	3	M	M	M	M	M	M	M	M	M	M	M	M	M;
M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	2	M	M	1	0	2	M	M	M	M	M	M	1	M	M	M	M	M	M	M	M	M	M	M	M;
M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	4	M	M	M	2	0	3	M	M	M	M	M	M	3	M	M	M	M	M	M	M	M	M	M	M;
M	M	M	M	M	M	M	10	M	M	M	M	M	M	M	M	M	M	M	M	M	3	0	M	M	M	M	M	M	M	2	M	M	M	M	M	M	M	M	M	M;
M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	3	M	M	M	M	M	0	1	M	M	M	M	M	M	M	M	M	M	M	9	M	M	M	M;
M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	2	M	M	M	M	1	0	6	M	M	M	M	M	3	M	M	M	M	M	M	M	M	M;
M	M	M	M	M	M	M	M	M	M	M	M	M	7	M	M	M	M	M	M	M	M	M	M	6	0	1	M	M	M	M	M	3	M	M	M	M	M	M	M	M;
M	M	M	M	M	M	M	M	M	M	M	M	M	M	8	M	M	M	M	M	M	M	M	M	M	1	0	3	M	M	M	M	M	M	M	M	M	M	M	M	M;
M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	3	M	M	M	M	M	M	3	0	2	M	M	M	M	M	4	M	M	M	M	M	M;
M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	1	M	M	M	M	M	M	2	0	2	M	M	M	M	M	M	M	M	M	M	M;
M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	3	M	M	M	M	M	M	2	0	1	M	M	M	M	1	M	M	M	M	M;
M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	2	M	M	M	M	M	M	1	0	M	M	M	M	M	M	M	M	M	6;
M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	3	M	M	M	M	M	M	0	7	M	M	M	4	M	M	M	M;
M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	3	M	M	M	M	M	7	0	3	M	M	M	3	M	M	M;
M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	3	0	3	M	M	M	2	M	M;
M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	4	M	M	M	M	M	3	0	5	M	M	M	1	M;
M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	1	M	M	M	M	5	0	M	M	M	M	2;
M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	9	M	M	M	M	M	M	M	4	M	M	M	M	0	5	M	M	M;
M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	3	M	M	M	5	0	1	M	M;
M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	2	M	M	M	1	0	2	M;
M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	1	M	M	M	2	0	6;
M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	6	M	M	M	M	2	M	M	M	6	0];
start=[1];
pick=[2,4];
throw=[3,5];
t=40;
go_on=true;
node=0;
[d]=generate_d(W);
[d_min,path_min]=dp_min(d,start,pick,throw);
disp(path_min)
%{
if d_min<t
    d_min
    path_min
    n=1
else
    while go_on
        node=node+1;
        number=[];
        for i=1:size(pick,2)
            number=[number,i];
        end
            a=nchoosek(pick,size(pick,2)-node);
            b=nchoosek(throw,size(pick,2)-node);
            d_step=[];
            for i=1:size(a,1)
                pick2=a(i,:);
                throw2=b(i,:);
                [d_min,path_min]=dp_min(d,start,pick2,throw2);
                d_step=[d_step,d_min];
            end  
            index=find(d_step==min(d_step));
            new_pick=a(index,:);
            new_throw=b(index,:);
            [d_min,path_min]=dp_min(d,start,new_pick,new_throw);
            if d_min<t
                d_min
                path_min
                n=node+1
                go_on=false;
                break;
            else
                continue;
            end
    end    
end    
%}
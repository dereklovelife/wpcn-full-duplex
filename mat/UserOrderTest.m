a = 79;
b = 65;
c = 95;

gamma = [a b c; a c b; b a c; b c a; b a c; b c a];
max_index = 0;
max_value = 0;
for i = 1: 6
    [~, t] = fairUserOrder(gamma(i,:));
    th(i) = sum(t);
    if(th(i) >= max_value)
        max_value = th(i);
        max_index = i;
    end
end
gamma(max_index,:)
th(max_index)

a = rand() * 100;
b = rand() * 100;
c = rand() * 100;

gamma = [a b c];
for i = 1: 6
    [~, t] = fairFindTTEST(gamma, i);
    th(i) = sum(t);
    if(th(i) >= max_value)
        max_value = th(i);
        max_index = i;
    end
end
figure(1)
plot(th);

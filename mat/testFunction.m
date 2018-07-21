Nr = input('天线数目');
Nt = Nr;
K = 4;
d = 3;
times = 1000;


sumth = zeros(1 ,6);
fairth = zeros(1, 6);
runtimes = zeros(1, 6);


for i = 1: times
    Hd = complex(normrnd(0, 1, K, Nt), normrnd(0, 1, K, Nt));
    Hu = complex(normrnd(0, 1, K, Nr), normrnd(0, 1, K, Nr));
    Hsi = complex(normrnd(0, 1, Nr, Nt), normrnd(0, 1, Nr, Nt));
    Hd = Hd / (d ^ 6) * 10 ^ 4;
    j = 1;
    try
        [sumSum, sumMin] = sumTh(Hd, Hu, Hsi);
        sumth(j) = sumth(j) + sumSum;
        fairth(j) = fairth(j) + sumMin;
        runtimes(j) = runtimes(j) + 1;
        j = j + 1;
    catch
        j = j + 1;
    end
    
    try
        [sumSum, sumMin] = sumTh_nosi(Hd, Hu, Hsi);
        sumth(j) = sumth(j) + sumSum;
        fairth(j) = fairth(j) + sumMin;
        runtimes(j) = runtimes(j) + 1;
        j = j + 1;
    catch
        j = j + 1;
    end
    
    try
        [sumSum, sumMin] = sumThHD(Hd, Hu, Hsi);
        sumth(j) = sumth(j) + sumSum;
        fairth(j) = fairth(j) + sumMin;
        runtimes(j) = runtimes(j) + 1;
        j = j + 1;
    catch
        j = j + 1;
    end
    
    try
        [sumSum, sumMin] = fair(Hd, Hu, Hsi);
        sumth(j) = sumth(j) + sumSum;
        fairth(j) = fairth(j) + sumMin;
        runtimes(j) = runtimes(j) + 1;
        j = j + 1;
    catch
        j = j + 1;
    end
    
    try
        [sumSum, sumMin] = fair_nosi(Hd, Hu, Hsi);
        sumth(j) = sumth(j) + sumSum;
        fairth(j) = fairth(j) + sumMin;
        runtimes(j) = runtimes(j) + 1;
        j = j + 1;
    catch
        j = j + 1;
    end
    
    try
        [sumSum, sumMin] = fairHD(Hd, Hu, Hsi);
        sumth(j) = sumth(j) + sumSum;
        fairth(j) = fairth(j) + sumMin;
        runtimes(j) = runtimes(j) + 1;
        j = j + 1;
    catch
        j = j + 1;
    end
end

fd = fopen('result.txt', 'a');
fprintf(fd, '\n');
fprintf(fd, 'antenna: %d \n', Nr);
for i = 1 : 6
    fprintf(fd, ' %d', runtimes(i));
end
fprintf(fd, '\n');
avgSum = sumth ./ runtimes;
avgFair = fairth ./ runtimes;

for i = 1 : 6
    fprintf(fd, ' %f', avgSum(i));
end
fprintf(fd, '\n');
for i = 1 : 6
    fprintf(fd, ' %f', avgFair(i));
end

fclose(fd);
% sumSum
% sumMin
% sumSumNO
% sumMinNO
% sumSumHD
% sumMinHD
% 
% minSum
% minMin
% minSumNO
% minMinNO
% minSumHD
% minMinHD
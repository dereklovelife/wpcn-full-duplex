%% 迭代求解全双工wpcn网络的吞吐量

%% Nt 发送天线数目

%% Nr 接收天线数目

%% K 用户数量

%% 先验证收敛性

%% 初始化

Nt = 3;
Nr = 3;
K = 4;

Hd = complex(normrnd(0, 1, K, Nt), normrnd(0, 1, K, Nt));
Hu = complex(normrnd(0, 1, K, Nr), normrnd(0, 1, K, Nr));
Hsi = complex(normrnd(0, 1, Nr, Nt), normrnd(0, 1, Nr, Nt));
% Hd =[
% 
%    1.0375 + 2.4304i,   1.8031 - 1.2265i,   1.7725 - 0.7994i;
%   -0.0204 - 0.4715i,   0.0530 + 0.7930i,  -2.5088 + 0.5670i;
%    0.6190 - 0.5603i,  -0.1779 - 2.1099i,  -0.4566 - 0.0014i;
% ];
% 
% Hu =[
%    0.6239 - 0.5375i,  -1.2874 - 1.9797i,   0.7833 + 0.8486i;
%    0.1264 + 0.3286i,   0.2181 - 1.8674i,  -0.3106 + 0.4052i;
%    0.6809 + 1.0541i,  -1.5666 - 1.8324i,   0.6553 - 0.7025i;
% ];
% 
% Hsi = [
% 
%    1.4990 - 0.8364i,  -1.0191 + 0.3023i,  -0.6011 - 0.9489i;
%    0.1378 + 0.8530i,  -1.3852 + 0.4158i,  -1.1719 + 0.5416i;
%   -1.5868 + 0.4773i,   0.9549 + 0.0430i,  -0.5771 - 0.8211i;
%   ];
% 初始化 St， t， 迭代 Sr
cvx_begin sdp quiet
    %cvx_precision low;
	variable St(Nt, Nt) hermitian semidefinite;
    %St == semidefinite(Nt);
	maximize(trace(Hd * St * Hd'));
	trace(St) <= 1;
	St >= 0;
cvx_end

%trace(Hd * St * Hd')
cvx_begin sdp quiet
    %cvx_precision low;
    variable Sr(Nr, Nr) hermitian semidefinite;
    maximize(trace(Hu' * Hu * Sr));
    trace(Sr) <= 1;
    Sr >= 0;
    trace(Sr * Hsi * St * Hsi') == 0;
cvx_end
%Sr
% 平均分配时隙
t = ones(1, K + 1);
t = t * (1 / (K + 1));
n = 4;
% th = zeros(1, n * 3);
th = zeros(1, n);
th2 = zeros(1, n);
th3 = zeros(1, n);
th5 = zeros(1, n);
th6 = zeros(1, n);
th7 = zeros(1, n);
t2 = t;
St2 = St;
Sr2 = Sr;

ret = getinit(St, Sr, t, Hd, Hu);
th(1) = sum(ret);
th2(1) = sum(ret);
% ue1(1) = ret(1);
% ue2(1) = ret(2);
% ue3(1) = ret(3);
t3 = t2;
St3 = ones(Nt, Nt) / Nt;
Sr3 = Sr2;
%% 判断是否收敛

t4 = t;
St4 = St;
Sr4 = Sr;


gamma = find_gamma_hd(Hu, Hd);
   
[~,tmp] = findTTest(gamma);
th4 = ones(1, n) * tmp;

j = 2;
for i = 2: n
    [Sr,~] = findSr(t, St, Hu, Hd, Hsi);
    [Sr2, ~] = findSr_nosi(t2, St2, Hu, Hd, Hsi);
    [Sr3, ~] = findSr(t3, St3, Hu, Hd, Hsi);
    [sr4, ~] = fairFindSr(t4, St4, Hu, Hd, Hsi);
    
%     [Sr, th(j)] = findSr(t, St, Hu, Hd, Hsi);
% 	j = j + 1; 
    
    [t, tmp] = findT(Sr, St, Hu, Hd, Hsi); 
    th(i) = sum(tmp);
    [t2, tmp2] = findT(Sr2,St2,Hu,Hd,Hsi);
    th2(i) = sum(tmp2);
    [t3, tmp3] = findT(Sr3, St3, Hu, Hd, Hsi);
    th3(i) = sum(tmp3);
    [t4, tmp4] = fairFindT(Sr4, St4, Hu, Hd, Hsi);
    th5(i) = sum(tmp4);
    th6(i) = min(tmp4);
    th7(i) = max(tmp4);
%     ue1(i) = tmp(1);
%     ue2(i) = tmp(2);
%     ue3(i) = tmp(3);

    
	
    

    [St, ~] = findSt(t, Sr, Hu, Hd, Hsi);
    
    
    
   
	[St2, ~] = findSt_nosi(t2, Sr2, Hu, Hd, Hsi);
    [St3, ~] = findSt(t3, Sr3, Hu, Hd, Hsi);
    
	
    
%     [t, th(j)] = findT(Sr, St, Hu, Hd, Hsi); 
%     j = j + 1; 
    
end


%j
%th
%Sr;
%St;
%t;
%real(Hd * St * Hd')
figure(1)
x = 1:1:n;
plot(th, '-rs')
hold on;
% plot(ue1, '-o');
% hold on;
% plot(ue2, '-x');
% hold on; 
% plot(ue3, '-+');
% hold on;
plot(th2, '-x');
hold on;
plot(th3, '-*');
hold on;
plot(th4, '-bs');

hold on;
plot(th5, '-+');
hold on;
plot(th6, '-*');
hold on;
plot(th7, '-s');
xlabel('Iteration times');
ylabel('Throughput(bit/Hz)');
%legend('Sum-throughput', 'UE1', 'UE2', 'UE3','No_SI','dsf','hd');
legend('Sum-throughput','no-si','dsf','hd','fair','fair_max','fair_min');
title('Iteration');
grid on;
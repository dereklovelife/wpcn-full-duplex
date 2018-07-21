function [th, thMin] = sumTh(Hu, Hd, Hsi)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
    [K, Nt] = size(Hd);
    [K, Nr] = size(Hu);
    
    %%³õÊ¼»¯
    cvx_begin sdp quiet
    %cvx_precision low;
        variable St(Nt, Nt) hermitian semidefinite;
    %St == semidefinite(Nt);
        maximize(trace(Hd * St * Hd'));
        trace(St) <= 1;
        St >= 0;
    cvx_end
    
    t = ones(1, K + 1);
    t = t * (1 / (K + 1));
    
    preTh = 0;
    
    %%µü´ú
    while (1 == 1)
        [Sr, ~] = findSr(t, St, Hu, Hd, Hsi);
        [St, ~] = findSt(t, Sr, Hu, Hd, Hsi);
        [t, tmp] = findT(Sr, St, Hu, Hd, Hsi);
        
        if (sum(tmp) - preTh) < 0.0005
            break
        end
        preTh = sum(tmp);
    end
    th = sum(tmp);
    thMin = min(tmp);
%     trace(Hsi' * Sr * Hsi * St)
    

end


function [th, thMin] = sumThHD(Hu, Hd, Hsi)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
    [K, Nt] = size(Hd);
    [K, Nr] = size(Hu);
    
    gamma = find_gamma_hd(Hu, Hd);
    [~, tmp] = findTHD(gamma);
    th = sum(tmp);
    thMin = min(tmp);
    
    

end


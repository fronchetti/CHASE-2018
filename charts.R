# Image type: EPS
# Image size: 700 x 520

# BP1 Closed
data_closed <- data.frame(row.names=c("atom_internals","atom_externals","electron_internals","electron_externals", "hubot_internals","hubot_externals","git-lfs_internals","git-lfs_externals", "linguist_internals","linguist_externals"), 
                meet=c(66,4,61,39,74,33,50,30,71,48), doesnt_meet=c(34,96,39,61,26,67,50,70,29,52))
data_closed <- do.call(rbind, data_closed)

par(mar=c(3,3,6,3))
barplot(data_closed, beside = FALSE, ylim=c(0,100), legend.text = c("Conform", "Doest not conform"), 
        args.legend = list(x = "top", ncol = 2, cex = 1.5, xpd = TRUE, inset = c(-0.17,-0.17)), names.arg = c("A1", "A2", "B1", "B2", "C1", "C2", "D1", "D2", "E1", "E2"), cex.names=1.2, cex.axis=1.2, ylab = "Percentage", cex.lab=1.2)

# BP1 Merged
data_merged <- data.frame(row.names=c("atom_internals","atom_externals","electron_internals","electron_externals", "hubot_internals","hubot_externals","git-lfs_internals","git-lfs_externals", "linguist_internals","linguist_externals"), 
                          meet=c(70,38,52,40,73,73,51,30,46,42), doesnt_meet=c(30,62,48,60,27,27,49,70,54,58))
data_merged <- do.call(rbind, data_merged)

barplot(data_merged, beside = FALSE, ylim=c(0,100), legend.text = c("Conform", "Doest not conform"), 
        args.legend = list(x = "top", ncol = 2, cex = 1.5, xpd = TRUE, inset = c(-0.17,-0.17)), names.arg = c("A1", "A2", "B1", "B2", "C1", "C2", "D1", "D2", "E1", "E2"), cex.names=1.2, cex.axis=1.2, ylab = "Percentage", cex.lab=1.2)

# BP2 Merged
data_merged <- data.frame(row.names=c("atom_internals","atom_externals","electron_internals","electron_externals", "hubot_internals","hubot_externals","git-lfs_internals","git-lfs_externals", "linguist_internals","linguist_externals"), 
                         meet=c(1,2, 1, 1, 8, 4, 40, 59, 20, 29), doesnt_meet=c(99, 98, 99, 99, 92, 96, 60, 41, 80, 71))
data_merged <- do.call(rbind, data_merged)
barplot(data_merged, beside = FALSE, ylim=c(0,100), legend.text = c("Conform", "Doest not conform"), 
        args.legend = list(x = "top", ncol = 2, cex = 1.5, xpd = TRUE, inset = c(-0.17,-0.17)), names.arg = c("A1", "A2", "B1", "B2", "C1", "C2", "D1", "D2", "E1", "E2"), cex.names=1.2, cex.axis=1.2, ylab = "Percentage", cex.lab=1.2)

# BP3 Merged
data_merged <- data.frame(row.names=c("atom_internals","atom_externals","electron_internals","electron_externals", "hubot_internals","hubot_externals","git-lfs_internals","git-lfs_externals", "linguist_internals","linguist_externals"), 
                          meet=c(8,8,13, 12,10,9,5,6,5,15), doesnt_meet=c(92,92,87,88,90,91,95,94,95,85))
data_merged <- do.call(rbind, data_merged)
barplot(data_merged, beside = FALSE, ylim=c(0,100), legend.text = c("Conform", "Doest not conform"), 
        args.legend = list(x = "top", ncol = 2, cex = 1.5, xpd = TRUE, inset = c(-0.17,-0.17)), names.arg = c("A1", "A2", "B1", "B2", "C1", "C2", "D1", "D2", "E1", "E2"), cex.names=1.2, cex.axis=1.2, ylab = "Percentage", cex.lab=1.2)

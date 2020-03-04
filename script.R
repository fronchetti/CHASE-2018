
project <- "electron"
closed_file_path <- paste("/home/fronchetti/Documentos/CHASE-2018/Dataset/", project, "/closed_pull_requests_summary.csv", sep="")
merged_file_path <- paste("/home/fronchetti/Documentos/CHASE-2018/Dataset/", project, "/merged_pull_requests_summary.csv", sep="")

# Best pratice 3
# Merged
merged_file <- read.csv(merged_file_path)
bp3_internals_merged_in <- subset(merged_file, user_type == "Internals" & (second_line_is_blank == "True"))
bp3_externals_merged_in <- subset(merged_file, user_type == "Externals" & (second_line_is_blank == "True"))
bp3_internals_merged_out <- subset(merged_file, user_type == "Internals" & (second_line_is_blank != "True"))
bp3_externals_merged_out <- subset(merged_file, user_type == "Externals" & (second_line_is_blank != "True")) 

# Closed
closed_file <- read.csv(closed_file_path)
bp3_internals_closed_in <- subset(closed_file, user_type == "Internals" & (number_of_characters <= 50 & second_line_is_blank == "True" & language == "en"))
bp3_externals_closed_in <- subset(closed_file, user_type == "Externals" & (number_of_characters <= 50 & second_line_is_blank == "True" & language == "en"))
bp3_internals_closed_out <- subset(closed_file, user_type == "Internals" & (number_of_characters > 50 | second_line_is_blank != "True" | language != "en"))
bp3_externals_closed_out <- subset(closed_file, user_type == "Externals" & (number_of_characters > 50 | second_line_is_blank != "True" | language != "en"))

# Best pratice 2
closed_file <- read.csv(closed_file_path)
bp2_internals_closed_in <- subset(closed_file, user_type == "Internals" & number_of_test_files > 0)
bp2_externals_closed_in <- subset(closed_file, user_type == "Externals" & number_of_test_files > 0)
bp2_internals_closed_out <- subset(closed_file, user_type == "Internals" & number_of_test_files == 0)
bp2_externals_closed_out <- subset(closed_file, user_type == "Externals" & number_of_test_files == 0)

# Merged
merged_file <- read.csv(merged_file_path)
bp2_internals_merged_in <- subset(merged_file, user_type == "Internals" & number_of_test_files > 0)
bp2_externals_merged_in <- subset(merged_file, user_type == "Externals" & number_of_test_files > 0)
bp2_internals_merged_out <- subset(merged_file, user_type == "Internals" & number_of_test_files == 0)
bp2_externals_merged_out <- subset(merged_file, user_type == "Externals" & number_of_test_files == 0)

# Best pratice 1
# Closed
closed_file <- read.csv(closed_file_path)
bp1_internals_closed_in <- subset(closed_file, user_type == "Internals" & (number_of_files_changed <= 2 & number_of_additions <= 20))
bp1_externals_closed_in <- subset(closed_file, user_type == "Externals" & (number_of_files_changed <= 2 & number_of_additions <= 20))
bp1_internals_closed_out <- subset(closed_file, user_type == "Internals" & (number_of_files_changed > 2 | number_of_additions > 20))
bp1_externals_closed_out <- subset(closed_file, user_type == "Externals" & (number_of_files_changed > 2 | number_of_additions > 20))

# Merged
merged_file <- read.csv(merged_file_path)
bp1_internals_merged_in <- subset(merged_file, user_type == "Internals" & (number_of_files_changed <= 2 & number_of_additions <= 20))
bp1_externals_merged_in <- subset(merged_file, user_type == "Externals" & (number_of_files_changed <= 2 & number_of_additions <= 20))
bp1_internals_merged_out <- subset(merged_file, user_type == "Internals" & (number_of_files_changed > 2 | number_of_additions > 20))
bp1_externals_merged_out <- subset(merged_file, user_type == "Externals" & (number_of_files_changed > 2 | number_of_additions > 20))

# > 100 days

for (project in c("atom","hubot","linguist","git-lfs","electron")){
  closed_file_path <- paste("/home/fronchetti/Documentos/CHASE-2018/Dataset/", project, "/closed_pull_requests_summary.csv", sep="")
  merged_file_path <- paste("/home/fronchetti/Documentos/CHASE-2018/Dataset/", project, "/merged_pull_requests_summary.csv", sep="")
  closed_file <- read.csv(closed_file_path)
  merged_file <- read.csv(merged_file_path)
  
  closed_file_output_path <- paste("/home/fronchetti/Documentos/CHASE-2018/Dataset/", project, "/", project, "_100_closed.csv", sep="")
  merged_file_output_path <- paste("/home/fronchetti/Documentos/CHASE-2018/Dataset/", project, "/", project, "_100_merged.csv", sep="")
  days_closed <- subset(closed_file, number_of_days > 100)
  days_merged <- subset(merged_file, number_of_days > 100)
  write.csv(days_closed, file = closed_file_output_path)
  write.csv(days_merged, file = merged_file_output_path)
}



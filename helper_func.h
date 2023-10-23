#define MAX_CONFIG_WORDS 100   // maximum number of words in a string
#define MAX_CONFIG_WORD_LEN 50 // maximum length of each word
#define MAX_LINE_LENGTH 100
#define MAX_ARG_LENGTH 100
#define START_PORT 3000

//split the config string into words
void splitStringBySpaces(const char* str, char output[][MAX_CONFIG_WORD_LEN], int* count) {
    int i = 0;
    const char* token = strtok((char*)str, " "); //] ensure original string isn't const

    while (token != NULL && i < MAX_CONFIG_WORDS) {
        strncpy(output[i], token, MAX_CONFIG_WORD_LEN);
        output[i][MAX_CONFIG_WORD_LEN-1] = '\0'; // ensure null-termination
        token = strtok(NULL, " ");
        i++;
    }
    *count = i;
}

door_access_t* appendValueDoor(door_access_t* door_arr, int size) {
    // Reallocate memory to increase size by 1
    door_access_t* newArr = realloc(door_arr, (size + 1) * sizeof(door_access_t));
    if (newArr == NULL) {
        perror("Failed to reallocate memory");
        exit(1);
    }
    return newArr;
}

int countLines(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Failed to open the file");
        return -1;
    }

    int ch;
    long lines = 0;
    while ((ch = fgetc(file)) != EOF) {
        if (ch == '\n') {
            lines++;
        }
    }

    fclose(file);
    return lines;
}
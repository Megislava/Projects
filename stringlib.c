#include "stringlib.h"
#include <stdio.h>

unsigned int stringLength(const char source[])
{
    int i = 0;
    while (source[i] != '\0') {
        i++;
    }
    return i;
}

char toLowerCase(char i)
{
    if (i >= 'A' && i <= 'Z') {
        i += 32;
    }
    return i;
}

int isPalindrome(const char source[])
{
    int i = 0;
    int j = (stringLength(source)) - 1;
    while (i < j) {
        while (source[i] == ' ' || source[i] == '\t' || source[i] == '\n') {
            i++;
        }
        while (source[j] == ' ' || source[j] == '\t' || source[j] == '\n') {
            j--;
        }
        if (toLowerCase(source[i]) != toLowerCase(source[j])) {
            return 0;
        }
        i++;
        j--;
    }
    return 1;
}

int rotateString(const char source[], char destination[], int number)
{
    int length = stringLength(source);
    if (number < 0) {
        return -1;
    }
    if (length == 0) {
        return 0;
    }
    for (int i = 0; i < length; i++) {
        destination[(number + i) % length] = source[i];

    }
    return number % length;
}

int printEnv(const char *env[], char separator[])
{
    int pos;
    for (pos = 0; env[pos] != NULL; pos++) {
        printf("%s%s", env[pos], separator);
    }
    return pos;
}

int gcd(int length, int cipher)
{
    int help = length + 1;
    if (help < 1 || cipher < 1) {
        return -1;
    }
    while (help != cipher) {
        if (help > cipher) {
            help -= cipher;
        } else {
            cipher -= help;
        }
    }
    return help;
}

int encryptString(const char source[], char destination[], int cipher)
{
    int length = stringLength(source);
    if (gcd(length, cipher) == 1 && cipher > 0) {
        for (int i = 0; i < length; i++) {
            int j = (cipher * (i + 1) - 1) % (length + 1);
            destination[j] = source[i];
        }
        return 0;
    }
    return -1;
}

int decryptString(const char source[], char destination[], int cipher)
{
    int length = stringLength(source);
    if (gcd(length, cipher) == 1 && cipher > 0) {
        int dec;
        for (dec = 1; dec < (length + 1); dec++) {
            if ((dec * cipher) % (length + 1) == 1) {
                break;
            }
        }
        for (int i = 0; i < length; i++) {
            int j = (dec * (i + 1) - 1) % (length + 1);
            destination[j] = source[i];
        }
        return 0;
    }
    return -1;
}

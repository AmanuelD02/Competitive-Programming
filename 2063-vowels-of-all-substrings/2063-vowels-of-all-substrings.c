
bool isVowel(char ch);

long long countVowels(char * word){
    long total = 0;
    int length = strlen(word);
    for(int i=0; i < length; i++){
        if (isVowel(word[i])) {
            total += (long)(i + 1) * (long)(length - i); 
        }
    }
    
    return total;
    
}

bool isVowel(char ch) {
    return ch =='a' || ch =='e' || ch =='i'  || ch =='o'  || ch =='u';
}
/^!/ {
    split($0, array, "!");
    command = array[2];
    while (command | getline line) {
        print(line);
    }
    close(command);
    next;
}

{
    print($0);
}

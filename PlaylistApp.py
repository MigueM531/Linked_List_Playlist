from LinkedList import DNode, DoubleLinkedList
import time


class Song:
    # def __init__(self, title, artist, duration):
    #     self.title: str = title
    #     self.artist: str = artist
    #     self.duration = duration

    
    def create_song(self):
        self.title = input("Título de la canción: ")
        self.artist = input("Artista:")
        self.duration = input("Duración")
        return Song

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.duration}s)"
    

class Node:
    def __init__(self, value, next = None, prev = None):
        self.value: Song = value
        self.next = next
        self.prev = prev

class PlayList:
    def __init__(self, head = None, tail = None):
        self.head: Node = head
        self.tail: Node = tail
        self.size = 0

    def add_song(self, value):
        new_song = Node(value)
        pass


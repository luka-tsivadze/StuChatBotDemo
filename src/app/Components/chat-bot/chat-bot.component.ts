import {
  Component,
  ElementRef,
  OnInit,
  ViewChild,
  Renderer2,
} from '@angular/core';
import { ApiService } from '../../Service/api.service';
import { FormControl } from '@angular/forms';

interface ChatMessage {
  sender: string;
  message: string;
  id: number;
}

@Component({
  selector: 'app-chat-bot',
  templateUrl: './chat-bot.component.html',
  styleUrls: ['./chat-bot.component.scss'],
})
export class ChatBotComponent {
  question = 'გამარჯობა რით შემიძლია დაგეხმაროთ ?'; // Setting an initial question
  answer = '';
  userInput = new FormControl('');
  chatHistory: ChatMessage[] = [];
  lastMessageId = 0; // To keep track of message IDs
  @ViewChild('chatbox', { static: false }) chatbox: ElementRef;

  constructor(private apiService: ApiService, private renderer: Renderer2) {}

  sendMessage(message: string): void {
    if (message.trim()) {
      this.addMessage('user', message);
      this.apiService.sendUserMessage(message).subscribe(
        (response) => {
          console.log('Response:', response);
          this.answer = response.answer;
          this.addMessage('bot', this.answer);
        },
        (error) => {
          console.error('Error:', error);
        }
      );

      this.userInput.reset();
    }
  }

  addMessage(sender: string, message: string): void {
    const chatMessage: ChatMessage = {
      sender,
      message,
      id: ++this.lastMessageId,
    };
    this.chatHistory.push(chatMessage);

    setTimeout(() => {
      if (sender === 'bot') {
        this.applyTextAnimation(chatMessage.id);
        this.scrollChatToBottom();
      } else if (sender === 'user') {
        console.log('chatMessage');
      }
    }, 0);
  }

  applyTextAnimation(messageId: number): void {
    const chatboxEl = this.chatbox.nativeElement;
    const messageEl = chatboxEl.querySelector(
      `.bot-message[data-id="${messageId}"] span:not(.animated)`
    );

    if (messageEl) {
      const text = messageEl.innerText;
      messageEl.innerHTML = '';

      const lines = text.split('\n');
      let totalDelay = 0; // Accumulated delay for line animations

      lines.forEach((line, lineIndex) => {
        const words = line.split(' ');

        words.forEach((word, wordIndex) => {
          const wordElement = this.renderer.createElement('span');
          wordElement.className = 'animated-word';
          wordElement.textContent = word;

          // Calculate the animation delay based on line and word index
          const animationDelay = totalDelay + wordIndex * 0.1;
          this.renderer.setStyle(
            wordElement,
            'animation-delay',
            `${animationDelay}s`
          );
          this.renderer.appendChild(messageEl, wordElement);

          // Add a space after the word
          const spaceElement = this.renderer.createElement('span');
          spaceElement.textContent = ' ';
          this.renderer.appendChild(messageEl, spaceElement);
        });

        // Update totalDelay to include the current line's animation duration
        totalDelay += words.length * 0.1;

        // Add a line break element after each line except the last one
        if (lineIndex < lines.length - 1) {
          const lineBreakElement = this.renderer.createElement('br');
          this.renderer.appendChild(messageEl, lineBreakElement);
        }
      });

      // Mark this element as animated to prevent reanimation
      messageEl.classList.add('animated');
    }
  }

  scrollChatToBottom(): void {
    setTimeout(() => {
      const chatbox = this.chatbox.nativeElement;
      chatbox.scrollTop = chatbox.scrollHeight - 1200;
    }, 0);
  }

  copyToClipboard(message: string): void {
    navigator.clipboard
      .writeText(message)
      .then(() => {
        console.log('Message copied to clipboard');
      })
      .catch((err) => {
        console.error('Could not copy text: ', err);
      });
  }

  likeMessage(msg: ChatMessage): void {
    console.log('Liked message:', msg.message);
  }

  dislikeMessage(msg: ChatMessage): void {
    console.log('Disliked message:', msg.message);
  }

  validateGeorgianInput(event: any): void {
    const input = event.target;
    const value = input.value;
    const regex =
      /^[\u10A0-\u10FF\u2D00-\u2D2F0-9\s+\-*/=()<>.,\[\]{}%^&|~!@#$;:?]*$/;
    if (!regex.test(value)) {
      input.value = value.replace(
        /[^\u10A0-\u10FF\u2D00-\u2D2F0-9\s+\-*/=()<>.,\[\]{}%^&|~!@#$;:?]/g,
        ''
      );
    }
  }
}

class Grid {
    constructor(width, height) {
        this.width = width;
        this.height = height;
        this.grid = Array.from({ length: height }, () => Array(width).fill(null));
    }

    placeFigure(figure) {
        for (let col = figure.position.x; col < figure.position.x + figure.size; col++) {
            for (let row = this.height - 1; row >= 0; row--) {
                if (this.grid[row][col] === null) {
                    this.grid[row][col] = figure.type;
                    return true; // Figure placed successfully
                }
            }
        }
        return false; // No space to place the figure
    }

    display() {
        console.log(this.grid.map(row => row.map(cell => cell || '.').join(' ')).join('\n'));
    }
}

class Figure {
    constructor(type, position, size) {
        this.type = type; // Type of figure (A, B, C, D, E)
        this.position = position; // { x: col, y: row }
        this.size = size; // Width of figure
    }
}

// Example usage:
const grid = new Grid(5, 5);
const figures = [
    new Figure('A', { x: 0, y: 0 }, 1),
    new Figure('B', { x: 1, y: 0 }, 1),
    new Figure('C', { x: 2, y: 0 }, 1),
    new Figure('D', { x: 3, y: 0 }, 1),
    new Figure('E', { x: 4, y: 0 }, 1)
];

figures.forEach(figure => grid.placeFigure(figure));
grid.display();
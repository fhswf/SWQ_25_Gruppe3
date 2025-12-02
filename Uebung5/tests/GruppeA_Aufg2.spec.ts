// Autoren: FARN und DLWG
import { test, expect, type Page } from '@playwright/test';

// Konstanten für die Testdaten und Locators
const TODO_INPUT_NAME = 'What needs to be done?';
const TODO_ITEMS = {
    LAUNDRY: 'Wäsche waschen',
    DISHES: 'Spülen',
    GYM: 'Gym',
    MOM_VISIT: 'Mama besuchen',
};

/**
 * Fügt ein einzelnes Todo-Item hinzu.
 * @param page - Die aktuelle Playwright Page Instanz.
 * @param text - Der Text des hinzuzufügenden Items.
 */
async function addTodo(page: Page, text: string) {
    // Verwendung des Locators aus Ihrer Vorgabe
    const input = page.getByRole('textbox', { name: TODO_INPUT_NAME }); 
    await input.click();
    await input.fill(text);
    await input.press('Enter');
}

// Hilfsfunktion zum Abrufen eines Todo-Listenelements
function getTodoItem(page: Page, itemText: string) {
    return page.getByRole('listitem').filter({ hasText: itemText });
}

test.beforeEach(async ({ page }) => {
    // Navigiert vor jedem Test zur Startseite
    await page.goto('https://demo.playwright.dev/todomvc/#/');
});

// -------------------------------------------------------------------

test.describe('TodoMVC Tests in Deutsch', () => {

    test('Szenario: Todos hinzufügen, löschen, markieren und löschen', async ({ page }) => {
        const { LAUNDRY, DISHES, GYM, MOM_VISIT } = TODO_ITEMS;
        
        const todoList = page.locator('.todo-list');
        const toggleAll = page.getByLabel('Mark all as complete');
        const clearCompletedButton = page.getByRole('button', { name: 'Clear completed' });

        // --- Teil 1: Todos erstellen, einen löschen und Zustand prüfen ---

        // Füge "Wäsche waschen" und "Spülen" einzeln hinzu
        await addTodo(page, LAUNDRY); 
        await addTodo(page, DISHES);

        // Prüfen, ob beide Items in der Liste sind
        await expect(todoList).toContainText(LAUNDRY);
        await expect(todoList).toContainText(DISHES);
        await expect(page.locator('.todo-count')).toContainText('2 items left');

        // "Wäsche waschen" löschen
        await getTodoItem(page, LAUNDRY).hover();
        await getTodoItem(page, LAUNDRY).getByRole('button', { name: 'Delete' }).click();

        // Prüfen, ob "Wäsche waschen" entfernt wurde
        await expect(todoList).not.toContainText(LAUNDRY);
        await expect(page.locator('.todo-count')).toContainText('1 item left');


        // --- Teil 2: Weitere Todos hinzufügen und alles markieren/entmarkieren ---

        // Füge "Gym" und "Mama besuchen" einzeln hinzu
        await addTodo(page, GYM);
        await addTodo(page, MOM_VISIT);

        // Prüfen des Gesamtbestands (3 Todos)
        await expect(page.locator('.todo-count')).toContainText('3 items left');

        // Alle Todos als erledigt markieren
        await toggleAll.click();

        // Prüfen, ob alle Todos abgeschlossen sind
        await expect(getTodoItem(page, DISHES).getByRole('checkbox')).toBeChecked();
        await expect(getTodoItem(page, GYM).getByRole('checkbox')).toBeChecked();
        await expect(getTodoItem(page, MOM_VISIT).getByRole('checkbox')).toBeChecked();
        await expect(page.locator('.todo-count')).toContainText('0 items left');

        // ... (Der Rest des Tests bleibt funktional identisch, verwendet aber die präziseren Locators)

        // "Spülen" entmarkieren
        await getTodoItem(page, DISHES).getByRole('checkbox').uncheck();
        await expect(page.locator('.todo-count')).toContainText('1 item left');

        // Nochmal Mark all (sollte alle als erledigt markieren)
        await toggleAll.click();
        await expect(page.locator('.todo-count')).toContainText('0 items left');
        
        // Nochmal Mark all (sollte alle als unerledigt markieren)
        await toggleAll.click();
        await expect(page.locator('.todo-count')).toContainText('3 items left');

        // --- Teil 3: Einzeln markieren und abgeschlossene löschen ---

        // "Spülen" markieren
        await getTodoItem(page, DISHES).getByRole('checkbox').check();
        await expect(page.locator('.todo-count')).toContainText('2 items left');
        await expect(clearCompletedButton).toBeVisible();

        // Abgeschlossene Todos löschen
        await clearCompletedButton.click();

        // Prüfen, ob "Spülen" entfernt wurde und die anderen zwei noch da sind
        await expect(todoList).not.toContainText(DISHES);
        await expect(page.locator('.todo-count')).toContainText('2 items left');
        await expect(clearCompletedButton).not.toBeVisible();
    });
});
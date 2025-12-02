// Autor: FARN
import { expect, test } from '@playwright/test';

test.describe('Aufgabe 3', () => {
  const baseUrl = 'https://demo.playwright.dev/todomvc/#/';

  test.beforeEach(async ({ page }) => {
    await page.goto(baseUrl);
    // Alle bestehenden Todos löschen, auch bei verzögertem Entfernen
    while (await page.locator('.todo-list li').count() > 0) {
      const todoCount = await page.locator('.todo-list li').count();
      for (let i = 0; i < todoCount; i++) {
        const todo = page.locator('.todo-list li').nth(0);
        await todo.hover();
        await todo.locator('.destroy').click({ force: true });
        await expect(todo).toBeHidden();
      }
    }
  });

  test('Filter "All", "Active", "Completed" zeigen die richtigen Todos an und Counter ist korrekt', async ({ page }) => {
    // Drei Todos anlegen
    const todos = ['Wäsche waschen', 'Spülen', 'Mama besuchen'];
    for (const todoText of todos) {
      await page.locator('.new-todo').fill(todoText);
      await page.keyboard.press('Enter');
    }

    // „Spülen“ als erledigt markieren
    await page.locator('.todo-list li').filter({ hasText: 'Spülen' }).locator('.toggle').check();

    // Filter „All“: Alle drei sichtbar
    await page.getByRole('link', { name: 'All' }).click();
    const allTodos = await page.locator('.todo-list li').allTextContents();
    expect(allTodos).toEqual(expect.arrayContaining(todos));
    // Counter: 2 items left
    await expect(page.locator('.todo-count')).toHaveText(/2 items left/);

    // Filter „Active“: Nur nicht erledigte
    await page.getByRole('link', { name: 'Active' }).click();
    const activeTodos = await page.locator('.todo-list li').allTextContents();
    expect(activeTodos).toEqual(expect.arrayContaining(['Wäsche waschen', 'Mama besuchen']));
    expect(activeTodos).not.toContain('Spülen');
    // Counter: 2 items left
    await expect(page.locator('.todo-count')).toHaveText(/2 items left/);

    // Filter „Completed“: Nur erledigte
    await page.getByRole('link', { name: 'Completed' }).click();
    const completedTodos = await page.locator('.todo-list li').allTextContents();
    expect(completedTodos).toEqual(['Spülen']);
    // Counter bleibt: 2 items left
    await expect(page.locator('.todo-count')).toHaveText(/2 items left/);
  });
});

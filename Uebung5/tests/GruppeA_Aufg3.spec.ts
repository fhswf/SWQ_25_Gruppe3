// Autoren: FARN und DLWG

import { test, expect } from '@playwright/test';
test('test', async ({ page }) => {
  await page.goto('https://demo.playwright.dev/todomvc/#/');
// Todos anlegen
  await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
  await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Wäsche waschen');
  await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
  await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Spülen');
  await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
  await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Mama besuchen');
  await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
  await page.getByRole('link', { name: 'All' }).click();
  await expect(page.locator('body')).toContainText('This is just a demo of TodoMVC for testing, not the real TodoMVC app. todosMark all as completeWäsche waschenSpülenMama besuchen3 items leftAll Active Completed Double-click to edit a todo Created by Remo H. Jansen Part of TodoMVC');
  await page.getByRole('listitem').filter({ hasText: 'Spülen' }).getByLabel('Toggle Todo').check();
  await page.getByRole('link', { name: 'Active' }).click();
  await expect(page.locator('body')).toContainText('This is just a demo of TodoMVC for testing, not the real TodoMVC app. todosMark all as completeWäsche waschenMama besuchen2 items leftAll Active Completed Double-click to edit a todo Created by Remo H. Jansen Part of TodoMVC');
  
})
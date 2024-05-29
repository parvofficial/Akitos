from __future__ import annotations

import discord
from discord.ext import menus
from discord.ext import commands
from .paginator import Paginator as HackerPaginator
from discord.ext.commands import Context, Paginator as CmdPaginator
from typing import Any


class FieldPagePaginator(menus.ListPageSource):

    def __init__(self,
                 entries: list[tuple[Any, Any]],
                 *,
                 per_page: int = 10,
                 inline: bool = False,
                 **kwargs) -> None:
        super().__init__(entries, per_page=per_page)
        self.embed: discord.Embed = discord.Embed(
            title=kwargs.get('title'),
            description=kwargs.get('description'),
            color=0x01f5b6)
        self.inline: bool = inline

    async def format_page(self, menu: HackerPaginator,
                          entries: list[tuple[Any, Any]]) -> discord.Embed:
        self.embed.clear_fields()

        for key, value in entries:
            self.embed.add_field(name=key, value=value, inline=self.inline)

        maximum = self.get_max_pages()
        if maximum > 1:
            text = f'Akito • Page {menu.current_page + 1}/{maximum}'
            self.embed.set_footer(
                text=text,
                icon_url=
                "https://media.discordapp.net/attachments/1167688002252853250/1173169144418545695/Picsart_23-11-12_10-07-30-575.png?ex=6562f9e8&is=655084e8&hm=48d9c6b2e7d5b41a317b0948d00e9e650ffc20333fe9f3bf0c2efcc0b33c0895&"
            )
            self.embed.timestamp = discord.utils.utcnow()
        return self.embed


class TextPaginator(menus.ListPageSource):

    def __init__(self, text, *, prefix='```', suffix='```', max_size=2000):
        pages = CmdPaginator(prefix=prefix,
                             suffix=suffix,
                             max_size=max_size - 200)
        for line in text.split('\n'):
            pages.add_line(line)

        super().__init__(entries=pages.pages, per_page=1)

    async def format_page(self, menu, content):
        maximum = self.get_max_pages()
        if maximum > 1:
            return f'{content}\Akito • Page {menu.current_page + 1}/{maximum}'
        return content


class DescriptionEmbedPaginator(menus.ListPageSource):

    def __init__(self,
                 entries: list[Any],
                 *,
                 per_page: int = 10,
                 **kwargs) -> None:
        super().__init__(entries, per_page=per_page)
        self.embed: discord.Embed = discord.Embed(
            title=kwargs.get('title'),
            color=0x01f5b6,
        )

    async def format_page(self, menu: HackerPaginator,
                          entries: list[tuple[Any, Any]]) -> discord.Embed:
        self.embed.clear_fields()

        self.embed.description = '\n'.join(entries)
        self.embed.timestamp = discord.utils.utcnow()
        maximum = self.get_max_pages()
        if maximum > 1:
            text = f'Akito • Page {menu.current_page + 1}/{maximum}'
            self.embed.set_footer(
                text=text,
                icon_url=
                "https://media.discordapp.net/attachments/1167688002252853250/1173169144418545695/Picsart_23-11-12_10-07-30-575.png?ex=6562f9e8&is=655084e8&hm=48d9c6b2e7d5b41a317b0948d00e9e650ffc20333fe9f3bf0c2efcc0b33c0895&"
            )

        return self.embed

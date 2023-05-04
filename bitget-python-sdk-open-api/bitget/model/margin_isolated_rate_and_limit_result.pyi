# coding: utf-8

"""
    Bitget Open API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from bitget import schemas  # noqa: F401


class MarginIsolatedRateAndLimitResult(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            baseBorrowAble = schemas.BoolSchema
            baseCoin = schemas.StrSchema
            baseDailyInterestRate = schemas.StrSchema
            baseMaxBorrowableAmount = schemas.StrSchema
            baseTransferInAble = schemas.BoolSchema
            
            
            class baseVips(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['MarginIsolatedVipResult']:
                        return MarginIsolatedVipResult
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['MarginIsolatedVipResult'], typing.List['MarginIsolatedVipResult']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'baseVips':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'MarginIsolatedVipResult':
                    return super().__getitem__(i)
            baseYearlyInterestRate = schemas.StrSchema
            leverage = schemas.StrSchema
            quoteBorrowAble = schemas.BoolSchema
            quoteCoin = schemas.StrSchema
            quoteDailyInterestRate = schemas.StrSchema
            quoteMaxBorrowableAmount = schemas.StrSchema
            quoteTransferInAble = schemas.BoolSchema
            
            
            class quoteVips(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['MarginIsolatedVipResult']:
                        return MarginIsolatedVipResult
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['MarginIsolatedVipResult'], typing.List['MarginIsolatedVipResult']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'quoteVips':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'MarginIsolatedVipResult':
                    return super().__getitem__(i)
            quoteYearlyInterestRate = schemas.StrSchema
            symbol = schemas.StrSchema
            __annotations__ = {
                "baseBorrowAble": baseBorrowAble,
                "baseCoin": baseCoin,
                "baseDailyInterestRate": baseDailyInterestRate,
                "baseMaxBorrowableAmount": baseMaxBorrowableAmount,
                "baseTransferInAble": baseTransferInAble,
                "baseVips": baseVips,
                "baseYearlyInterestRate": baseYearlyInterestRate,
                "leverage": leverage,
                "quoteBorrowAble": quoteBorrowAble,
                "quoteCoin": quoteCoin,
                "quoteDailyInterestRate": quoteDailyInterestRate,
                "quoteMaxBorrowableAmount": quoteMaxBorrowableAmount,
                "quoteTransferInAble": quoteTransferInAble,
                "quoteVips": quoteVips,
                "quoteYearlyInterestRate": quoteYearlyInterestRate,
                "symbol": symbol,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["baseBorrowAble"]) -> MetaOapg.properties.baseBorrowAble: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["baseCoin"]) -> MetaOapg.properties.baseCoin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["baseDailyInterestRate"]) -> MetaOapg.properties.baseDailyInterestRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["baseMaxBorrowableAmount"]) -> MetaOapg.properties.baseMaxBorrowableAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["baseTransferInAble"]) -> MetaOapg.properties.baseTransferInAble: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["baseVips"]) -> MetaOapg.properties.baseVips: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["baseYearlyInterestRate"]) -> MetaOapg.properties.baseYearlyInterestRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["leverage"]) -> MetaOapg.properties.leverage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quoteBorrowAble"]) -> MetaOapg.properties.quoteBorrowAble: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quoteCoin"]) -> MetaOapg.properties.quoteCoin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quoteDailyInterestRate"]) -> MetaOapg.properties.quoteDailyInterestRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quoteMaxBorrowableAmount"]) -> MetaOapg.properties.quoteMaxBorrowableAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quoteTransferInAble"]) -> MetaOapg.properties.quoteTransferInAble: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quoteVips"]) -> MetaOapg.properties.quoteVips: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quoteYearlyInterestRate"]) -> MetaOapg.properties.quoteYearlyInterestRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["baseBorrowAble", "baseCoin", "baseDailyInterestRate", "baseMaxBorrowableAmount", "baseTransferInAble", "baseVips", "baseYearlyInterestRate", "leverage", "quoteBorrowAble", "quoteCoin", "quoteDailyInterestRate", "quoteMaxBorrowableAmount", "quoteTransferInAble", "quoteVips", "quoteYearlyInterestRate", "symbol", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["baseBorrowAble"]) -> typing.Union[MetaOapg.properties.baseBorrowAble, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["baseCoin"]) -> typing.Union[MetaOapg.properties.baseCoin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["baseDailyInterestRate"]) -> typing.Union[MetaOapg.properties.baseDailyInterestRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["baseMaxBorrowableAmount"]) -> typing.Union[MetaOapg.properties.baseMaxBorrowableAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["baseTransferInAble"]) -> typing.Union[MetaOapg.properties.baseTransferInAble, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["baseVips"]) -> typing.Union[MetaOapg.properties.baseVips, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["baseYearlyInterestRate"]) -> typing.Union[MetaOapg.properties.baseYearlyInterestRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["leverage"]) -> typing.Union[MetaOapg.properties.leverage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quoteBorrowAble"]) -> typing.Union[MetaOapg.properties.quoteBorrowAble, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quoteCoin"]) -> typing.Union[MetaOapg.properties.quoteCoin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quoteDailyInterestRate"]) -> typing.Union[MetaOapg.properties.quoteDailyInterestRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quoteMaxBorrowableAmount"]) -> typing.Union[MetaOapg.properties.quoteMaxBorrowableAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quoteTransferInAble"]) -> typing.Union[MetaOapg.properties.quoteTransferInAble, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quoteVips"]) -> typing.Union[MetaOapg.properties.quoteVips, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quoteYearlyInterestRate"]) -> typing.Union[MetaOapg.properties.quoteYearlyInterestRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> typing.Union[MetaOapg.properties.symbol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["baseBorrowAble", "baseCoin", "baseDailyInterestRate", "baseMaxBorrowableAmount", "baseTransferInAble", "baseVips", "baseYearlyInterestRate", "leverage", "quoteBorrowAble", "quoteCoin", "quoteDailyInterestRate", "quoteMaxBorrowableAmount", "quoteTransferInAble", "quoteVips", "quoteYearlyInterestRate", "symbol", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        baseBorrowAble: typing.Union[MetaOapg.properties.baseBorrowAble, bool, schemas.Unset] = schemas.unset,
        baseCoin: typing.Union[MetaOapg.properties.baseCoin, str, schemas.Unset] = schemas.unset,
        baseDailyInterestRate: typing.Union[MetaOapg.properties.baseDailyInterestRate, str, schemas.Unset] = schemas.unset,
        baseMaxBorrowableAmount: typing.Union[MetaOapg.properties.baseMaxBorrowableAmount, str, schemas.Unset] = schemas.unset,
        baseTransferInAble: typing.Union[MetaOapg.properties.baseTransferInAble, bool, schemas.Unset] = schemas.unset,
        baseVips: typing.Union[MetaOapg.properties.baseVips, list, tuple, schemas.Unset] = schemas.unset,
        baseYearlyInterestRate: typing.Union[MetaOapg.properties.baseYearlyInterestRate, str, schemas.Unset] = schemas.unset,
        leverage: typing.Union[MetaOapg.properties.leverage, str, schemas.Unset] = schemas.unset,
        quoteBorrowAble: typing.Union[MetaOapg.properties.quoteBorrowAble, bool, schemas.Unset] = schemas.unset,
        quoteCoin: typing.Union[MetaOapg.properties.quoteCoin, str, schemas.Unset] = schemas.unset,
        quoteDailyInterestRate: typing.Union[MetaOapg.properties.quoteDailyInterestRate, str, schemas.Unset] = schemas.unset,
        quoteMaxBorrowableAmount: typing.Union[MetaOapg.properties.quoteMaxBorrowableAmount, str, schemas.Unset] = schemas.unset,
        quoteTransferInAble: typing.Union[MetaOapg.properties.quoteTransferInAble, bool, schemas.Unset] = schemas.unset,
        quoteVips: typing.Union[MetaOapg.properties.quoteVips, list, tuple, schemas.Unset] = schemas.unset,
        quoteYearlyInterestRate: typing.Union[MetaOapg.properties.quoteYearlyInterestRate, str, schemas.Unset] = schemas.unset,
        symbol: typing.Union[MetaOapg.properties.symbol, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MarginIsolatedRateAndLimitResult':
        return super().__new__(
            cls,
            *args,
            baseBorrowAble=baseBorrowAble,
            baseCoin=baseCoin,
            baseDailyInterestRate=baseDailyInterestRate,
            baseMaxBorrowableAmount=baseMaxBorrowableAmount,
            baseTransferInAble=baseTransferInAble,
            baseVips=baseVips,
            baseYearlyInterestRate=baseYearlyInterestRate,
            leverage=leverage,
            quoteBorrowAble=quoteBorrowAble,
            quoteCoin=quoteCoin,
            quoteDailyInterestRate=quoteDailyInterestRate,
            quoteMaxBorrowableAmount=quoteMaxBorrowableAmount,
            quoteTransferInAble=quoteTransferInAble,
            quoteVips=quoteVips,
            quoteYearlyInterestRate=quoteYearlyInterestRate,
            symbol=symbol,
            _configuration=_configuration,
            **kwargs,
        )

from bitget.model.margin_isolated_vip_result import MarginIsolatedVipResult
    # -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 01:02:02 2020

@author: Matheus Yokoyama
"""
# https://www.kaggle.com/olistbr/brazilian-ecommerce


#Merge dos dados de 
import pandas as pd

# Base de pagamento dos pedidos
# Contém ID_Pedido, Qtd de forma realizado no pagamento, tipo pagamento, Qtd_parcela, valor pagamento.
df1 = pd.read_csv("D:/Dados/e-commerce_Brazil/olist_order_payments_dataset.csv")

# Base de Pedidos.
# Contém ID_pedido, ID_cliente, Status_pedido, Data_pedido, Data_aprovação_pedido,
# Data_saida_entrega, Data_entregue_cliente, Data_estimado_entrega
df2 = pd.read_csv("D:/Dados/e-commerce_Brazil/olist_orders_dataset.csv")

merge = pd.merge(df1,df2)

# Base de reviews pedidos
df3 = pd.read_csv("D:/Dados/e-commerce_Brazil/olist_order_reviews_dataset.csv")

merge = pd.merge(merge,df3)

# Base de produtos no pedido
# ID_pedido, Qtd_produto_igual_pedido, ID_produto, ID_vendedora, Data_limite_despacho, Preço_produto, Valor_frete
df4 = pd.read_csv("D:/Dados/e-commerce_Brazil/olist_order_items_dataset.csv")

merge = pd.merge(merge, df4)

#%%


merge.pop("order_delivered_carrier_date")
#merge.pop("order_purchase_timestamp")
merge.pop("order_delivered_customer_date")
merge.pop("order_estimated_delivery_date")
merge.pop("review_comment_message")
merge.pop("review_creation_date")
merge.pop("review_answer_timestamp")
merge.pop("shipping_limit_date")
merge.pop("review_comment_title")
merge.pop("order_approved_at")
merge.pop("review_id")
merge.pop("customer_id")
merge.pop("price")
merge.pop("freight_value")
merge.pop("payment_sequential")



#%%
status = pd.unique(merge["order_status"])
payment_type = pd.unique(merge["payment_type"])

merge.sort_values("order_id", inplace = True)


#%%

# Retira produtos duplicados
merge.drop_duplicates(subset="product_id", keep=False, inplace = True)

merge["payment_type"],payment_type = pd.factorize(merge["payment_type"])
merge["order_status"],status = pd.factorize(merge["order_status"])


#%%

credit = merge["payment_type"] == 0
credit = merge[credit & True]
#%%
order_id = merge.pop("order_id")
product_id = merge.pop("product_id")
seller_id = merge.pop("seller_id")

#%%


primeira_compra = pd.DataFrame.min(merge['order_purchase_timestamp'])
ultima_compra = pd.DataFrame.max(merge['order_purchase_timestamp'])
merge['order_purchase_timestamp'] = merge['order_purchase_timestamp'].astype('datetime64')
merge['order_purchase_timestamp'].dt.year


#%%

merge['valor'] = merge.apply(lambda x: pd.Series([1], index = ['valor']), axis = 1)
merge.groupby(merge['order_purchase_timestamp'])['valor'].agg('sum')

#%%
import seaborn as sn
 
sn.regplot(merge['order_purchase_timestamp'], )


#%%

nova_coluna = ['id_pedido', '']

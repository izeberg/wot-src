package net.wg.gui.lobby.storage.categories.cards
{
   import net.wg.data.Colors;
   import net.wg.gui.components.controls.IconText;
   import net.wg.gui.components.controls.VO.PriceVO;
   
   public class RestoreVehicleCard extends RestoreBaseCard
   {
       
      
      public function RestoreVehicleCard()
      {
         super();
      }
      
      override protected function drawPrice() : void
      {
         var _loc1_:PriceVO = Boolean(_data.price) ? _data.price.price.getPriceVO() : null;
         if(_loc1_)
         {
            price.text = App.utils.locale.integer(_loc1_.value);
            price.textColor = !!_data.isMoneyEnough ? Number(IconText.BASE_COLOR) : Number(Colors.ERROR_COLOR);
            price.icon = _loc1_.name;
            price.visible = true;
            price.invalidatePosition();
            price.validateNow();
         }
         else
         {
            price.visible = false;
         }
      }
   }
}

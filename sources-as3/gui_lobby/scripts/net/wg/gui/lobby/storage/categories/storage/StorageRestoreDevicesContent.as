package net.wg.gui.lobby.storage.categories.storage
{
   import net.wg.data.ListDAAPIDataProvider;
   import net.wg.data.constants.Linkages;
   import net.wg.gui.lobby.storage.categories.cards.CardEvent;
   import net.wg.gui.lobby.storage.categories.cards.RestoreDeviceCardVO;
   import net.wg.infrastructure.base.meta.impl.StorageRestoreDevicesContentMeta;
   import scaleform.clik.interfaces.IDataProvider;
   
   public class StorageRestoreDevicesContent extends StorageRestoreDevicesContentMeta
   {
       
      
      public function StorageRestoreDevicesContent()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         carousel.scrollList.itemRendererClassReference = Linkages.RESTORE_DEVICE_CARD_RENDERER;
      }
      
      override protected function updateBalanceLayout() : void
      {
         balance.x = carousel.x + carousel.width;
         balance.y = STATE_NORMAL_BALANCE_Y;
      }
      
      override protected function getNewCardDP() : IDataProvider
      {
         return new ListDAAPIDataProvider(RestoreDeviceCardVO);
      }
      
      override protected function onCardSellHandler(param1:CardEvent) : void
      {
         param1.stopImmediatePropagation();
         var _loc2_:RestoreDeviceCardVO = RestoreDeviceCardVO(param1.data);
         restoreItemS(_loc2_.id,_loc2_.restoreReason);
      }
   }
}

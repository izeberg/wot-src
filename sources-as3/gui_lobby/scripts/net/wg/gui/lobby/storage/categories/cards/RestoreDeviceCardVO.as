package net.wg.gui.lobby.storage.categories.cards
{
   import net.wg.gui.components.controls.VO.PriceVO;
   import net.wg.gui.components.paginator.vo.ToolTipVO;
   
   public class RestoreDeviceCardVO extends RestoreBaseCardVO
   {
      
      private static const IS_ENOUGH_STATUSES:String = "isEnoughStatuses";
      
      private static const INFO_TOOLTIP_DATA:String = "infoTooltipData";
       
      
      public var availableToRestore:String = "";
      
      public var isEnoughStatuses:Vector.<PriceVO> = null;
      
      public var restoreReason:int = 0;
      
      private var _infoTooltipData:ToolTipVO = null;
      
      public function RestoreDeviceCardVO(param1:Object)
      {
         super(param1);
      }
      
      override protected function onDataWrite(param1:String, param2:Object) : Boolean
      {
         var _loc3_:Array = null;
         var _loc4_:Array = null;
         if(IS_ENOUGH_STATUSES == param1)
         {
            if(param2)
            {
               if(this.isEnoughStatuses && this.isEnoughStatuses.length > 0)
               {
                  this.isEnoughStatuses.length = 0;
               }
               else
               {
                  this.isEnoughStatuses = new Vector.<PriceVO>();
               }
               _loc3_ = param2 as Array;
               if(_loc3_ != null)
               {
                  for each(_loc4_ in _loc3_)
                  {
                     this.isEnoughStatuses.push(new PriceVO(_loc4_));
                  }
               }
               else
               {
                  App.utils.asserter.assert(param2 is Array,param1 + " must be an Array");
               }
            }
            return false;
         }
         if(param1 == INFO_TOOLTIP_DATA)
         {
            this._infoTooltipData = new ToolTipVO(param2);
            return false;
         }
         return super.onDataWrite(param1,param2);
      }
      
      override protected function onDispose() : void
      {
         if(this.isEnoughStatuses)
         {
            this.isEnoughStatuses.length = 0;
            this.isEnoughStatuses = null;
         }
         if(this._infoTooltipData)
         {
            this._infoTooltipData.dispose();
            this._infoTooltipData = null;
         }
         super.onDispose();
      }
      
      public function get infoTooltipData() : ToolTipVO
      {
         return this._infoTooltipData;
      }
   }
}

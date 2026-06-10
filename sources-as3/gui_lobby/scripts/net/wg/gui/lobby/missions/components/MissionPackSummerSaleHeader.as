package net.wg.gui.lobby.missions.components
{
   import net.wg.gui.lobby.missions.components.headerComponents.SummerSaleHeaderDescBlock;
   import net.wg.gui.lobby.missions.components.headerComponents.SummerSaleHeaderTitleBlock;
   import net.wg.gui.lobby.missions.data.MissionPackSummerSaleHeaderVO;
   import scaleform.clik.constants.InvalidationType;
   
   public class MissionPackSummerSaleHeader extends MissionPackHeaderBase
   {
      
      private static const HEIGHT:int = 425;
      
      private static const HEIGHT_DISABLED:int = 300;
       
      
      public var descBlock:SummerSaleHeaderDescBlock;
      
      private var _summerSaleTitleBlock:SummerSaleHeaderTitleBlock;
      
      public function MissionPackSummerSaleHeader()
      {
         super();
         this._summerSaleTitleBlock = SummerSaleHeaderTitleBlock(titleBlock);
      }
      
      override protected function onDispose() : void
      {
         this.descBlock.dispose();
         this.descBlock = null;
         this._summerSaleTitleBlock = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         var _loc1_:MissionPackSummerSaleHeaderVO = null;
         super.draw();
         if(data && isInvalid(InvalidationType.DATA))
         {
            _loc1_ = MissionPackSummerSaleHeaderVO(data);
            height = !!_loc1_.isEnabled ? Number(HEIGHT) : Number(HEIGHT_DISABLED);
            this._summerSaleTitleBlock.isEnabled = _loc1_.isEnabled;
            this.descBlock.update(_loc1_.descBlockVO);
            this.descBlock.isEnabled = _loc1_.isEnabled;
            this.descBlock.validateNow();
         }
         if(isInvalid(InvalidationType.SIZE))
         {
            this.descBlock.width = width;
         }
      }
      
      override protected function get dataClass() : Class
      {
         return MissionPackSummerSaleHeaderVO;
      }
   }
}

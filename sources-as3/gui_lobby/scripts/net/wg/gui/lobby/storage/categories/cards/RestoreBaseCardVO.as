package net.wg.gui.lobby.storage.categories.cards
{
   public class RestoreBaseCardVO extends BaseCardVO
   {
       
      
      public var timerText:String = "";
      
      public var timerIcon:String = "";
      
      public function RestoreBaseCardVO(param1:Object)
      {
         super(param1);
      }
      
      override public function isEqual(param1:BaseCardVO) : Boolean
      {
         var _loc2_:RestoreBaseCardVO = param1 as RestoreBaseCardVO;
         if(_loc2_ == null)
         {
            return false;
         }
         return super.isEqual(_loc2_) && this.timerText == _loc2_.timerText && this.timerIcon == _loc2_.timerIcon;
      }
      
      override public function toString() : String
      {
         return "[RestoreBaseCardVO > id: " + id + ", image: " + image + "]";
      }
   }
}
